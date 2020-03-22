# coding=utf-8
from subprocess import call


minhaFala = "Olá Mundo, vamos sintetizar com python!"

call(["espeak", minhaFala])