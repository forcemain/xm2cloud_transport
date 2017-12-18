#! -*- coding: utf-8 -*-


import os
import sys
import logging.config

from agent import agent_dir
from agent.main import Agent


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, os.path.dirname(__file__))


# for logging
log_ini = os.path.join(agent_dir, 'conf', 'logging.ini')
logging.config.fileConfig(log_ini)


def create_app():
    _app = Agent(pull_interval=5, debug=True)

    return _app

if __name__ == '__main__':
    app = create_app()
    app.loop()
