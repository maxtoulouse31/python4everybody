{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs24 \cf0 import re\
name = raw_input("Enter file:")\
if len(name) < 1 : name = "mbox-short.txt"\
s = open(name, 'r')\
ss = s.read()\
counts = dict()\
for line in s:\
	words = line.split()\
	if len(words) < 2 or words [0] != 'From': continue\
	counts[words[1]] = counts.get(words[1], 0) + 1\
        \
bigcount = None\
bigname = None\
for countz in counts:\
	if bigcount == None or bigname < counts[countz]:\
		bigcount = countz\
		bigname = counts[countz]  \
\
print bigcount,bigname}