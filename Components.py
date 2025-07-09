from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.schema import AgentAction, AgentFinish, OutputParserException
from langchain.agents.agent import AgentOutputParser
from typing import Union
import re
import os
from dotenv import load_dotenv

load_dotenv()

class CodeOutputParser(AgentOutputParser):

    @property
    def _type(self) -> str:
        return 'custom_output_parser'

    def parse(self, llm_op: str) -> Union[AgentAction, AgentFinish]:
        if 'Final Answer:' in llm_op:
            return AgentFinish(
                return_values={'output': llm_op.split('Final Answer:')[-1]},
                log=llm_op
            )

        thought_match = re.search(r'Thought:\s*(.*?)(?=\nAction:|$)', llm_op, re.DOTALL)
        action_match = re.search(r'Action:\s*(.*?)(?=\nAction Input:|$)', llm_op, re.DOTALL)
        action_ip_match = re.search(r'Action Input:\s*(.*?)(?=\nObservation:|$)', llm_op, re.DOTALL)

        if not action_match:
            raise OutputParserException('can not parse llm outpit action match not found \n' + llm_op)

        action = action_match.group(1).strip()

        if action_ip_match:
            action_ip = action_ip_match.group(1).strip()

            if "```" in action_ip:
                code_match = re.search('```(?:python)?\s*(.*?)\s*```', action_ip, re.DOTALL)
                if code_match:
                    action_ip = code_match.group(1).strip()
                else:
                    action_ip = action_ip.replace("```python", "").replace("```", "").strip()
        else:
            action_ip = ""

        return AgentAction(
            tool=action,
            tool_input=action_ip,
            log=llm_op
        )


class PyCodeAgent:

    def __init__(self):
        self.gemini = ChatGoogleGenerativeAI(
            model = 'gemini-2.5-flash',
            temperature = 0.85,
            google_api_key = os.getenv("GOOGLE_API_KEY")
        )
        self.memory = ConversationBufferMemory(
            memory_key = 'chat_history',
            return_messages = True
        )
        self.prompt_text = '''You are a helpful python coding assistant. When asked to write code, you should:
            1. Think about what needs to be done
            2. Use the appropriate tool to generate the code
            3. Format your response properly
            4. Make sure to run a test case using the tools provided before returning the final answer
            5. The user receives only the Final Answer, so make sure it contains the code or python comments
            6. Don't include the test cases in the final answer, however these need to be included in concise comments at the end.
            7. For non coding questions, just write plain text in python, also motivate them to ask them only python questions.
            8. This is a project created by Divyansh Vishwkarma (GitHub - Divyansh900) repo named PyCodeAgent
            9. If only the output of the code is asked return the output in python comments as well.
            10. You can read, edit and write files in cwd -> files.
            11. Libraries in execution environment are already imported, so no need to write the import statement.
            13. If asked to do file related operations, don't use test cases, just carry out the operation on the specified file.
            14. For File operations, after performing the operations, just return completion status of operation in the python comments, but make sure to carry out the operation.
            15. During file operations make sure the specifics like column or file name exists and if list all of them and resolve the real names
            16. Always return a Final Answer on completion, its very very crucial
            17. You can't import any library, but some are already loaded in execution environment
            18. Before trying to use to library verify it exists using the tool
            
            Always respond in this format:
            Thought: [your reasoning]
            Action: [tool name]
            Action Input: [tool input]
            
            If the final code is found responds with
            Final Answer: [final answer code]
            
            Input : {prompt}
            '''

        self.prompt_temp = PromptTemplate(
            input_variables = ['prompt'],
            template = self.prompt_text
        )

        self.agent = self._init_agent()

    def _init_agent(self):

        def check_libs(library)->str:
            libraries = [
                'numpy', 'np',
                'pandas', 'pd',
                'matplotlib', 'matplotlib.pyplot', 'plt',
                'seaborn', 'sns'
            ]
            if library in libraries:
                return "Library is present. Hence no need to write the import statment for this library in the execution code."
            else:
                return f"library not found"

        check_lib = Tool(
            name = 'Libraries',
            description = 'Show if the libraries is already present in the execution environment that the agent can use, if not present its code can not be tested',
            func = check_libs
        )

        def run_code(code: str) -> str|None:
            """Execute Python code and return the result."""
            try:
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                import seaborn as sns
                import matplotlib

                matplotlib.use('Agg')

                # We only allow the agent these builtin keywords
                exec_globals = {
                    '__builtins__': {
                        'print': print,
                        'len': len,
                        'max': max,
                        'min': min,
                        'sum': sum,
                        'range': range,
                        'list': list,
                        'dict': dict,
                        'set': set,
                        'tuple': tuple,
                        'str': str,
                        'int': int,
                        'float': float,
                        'bool': bool,
                        'enumerate': enumerate,
                        'zip': zip,
                        'sorted': sorted,
                        'reversed': reversed,
                        'any': any,
                        'all': all,
                        'isinstance': isinstance,
                        'type': type,
                        'hasattr': hasattr,
                        'getattr': getattr,
                        'setattr': setattr,
                    },
                    'pd': pd,
                    'pandas': pd,
                    'np': np,
                    'numpy': np,
                    'seaborn': sns,
                    'sns' : sns,
                    'matplotlib' : plt,
                    'matplotlib.pyplot': plt,
                    'plt' : plt
                }
                exec_locals = {}

                # Capture output
                import io
                import sys
                old_stdout = sys.stdout
                sys.stdout = captured_output = io.StringIO()

                try:
                    exec(code, exec_globals, exec_locals)
                    output = captured_output.getvalue()
                    return output if output else "Code executed successfully (no output)"
                finally:
                    sys.stdout = old_stdout
            except Exception as e:
                return f"Error executing code: {str(e)}"

        code_runner = Tool(
            name = 'Run Code',
            description = 'Runs the code and return the output if any or any exception if any.',
            func = run_code
        )

        def calculate(expression: str) -> str:
            """Evaluate mathematical expressions."""
            try:
                result = eval(expression, {"__builtins__": {}}, {})
                return str(result)
            except Exception as e:
                return f"Error in calculation: {str(e)}"

        calculator = Tool(
            name = 'Calculator',
            description = 'Can be used to calculate simple mathematical expressions like 2+3/1',
            func = calculate
        )

        tools = [code_runner, calculator, check_lib]

        agent = initialize_agent(
            tools=tools,
            llm=self.gemini,
            memory=self.memory,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            agent_kwargs={'output_parser': CodeOutputParser()},
            verbose=True
        )
        return agent

    def generate(self, prompt: str)-> str:
        prompt = self.prompt_temp.format(prompt=prompt)
        res = self.agent.invoke({'input': prompt})
        return res.get('output')

    def reset_agent(self)-> None:
        self.agent = self._init_agent()
        self.memory.clear()

    def get_memory_size(self):
        return len(self.memory.chat_memory.messages)