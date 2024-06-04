#!/bin/bash

python -m venv venv

venv/bin/pip  install googletrans==4.0.0rc1

python -m venv venv-aai

venv-aai/bin/pip  install assemblyai

mkdir subtitles audio



