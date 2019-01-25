#!/usr/bin/env python
#coding:utf8
import re


def project(path):
	"""
	경로를 넣으면 project 이름을 반환한다.
	"""
	p = re.findall('/project/(\S[^/]+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로를 넣으면 seq 이름을 반환한다.
	"""
	p = re.findall('/shot/(\S[^/]+)', path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를 가지고 올 수 없습니다."
	return p[0], None

if __name__ == "__main__":
	path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"
	projectName, err = project(path)
	if err:
		print err
	print projectName

	s, err = seq(path)
	if err:
		print err
	print s

