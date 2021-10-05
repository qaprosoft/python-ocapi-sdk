import os
import sys

import configparser

import logging


class Provider(object):

    @property
    def config(self):
        config = configparser.ConfigParser()
        if len (config.read(os.path.join(os.getcwd(), '.pycapi'))) == 0:
            return None
        else:
            return config

    def get_properties(self, key):
        if self.config == None:
            return
        else:
            try:
                return self.config.get('default', key)
            #except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
            except:
                logging.exception('\n\nYou must either specify configs in a .pycapi file or supply args in an API instance\n\n')