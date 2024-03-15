#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source('jmp1.nasm'))
def test_jmp1_if():
    ram = {0: 0, 1: 0}
    tst = {0: 1}
    assert nasm_test("jmp1.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp1.nasm'))
def test_jmp1_else():
    ram = {0: 0, 1: 3}
    tst = {0: 2}
    assert nasm_test("jmp1.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp2.nasm'))
def test_jmp2_if():
    ram = {0: 0, 1: 3}
    tst = {0: 1}
    assert nasm_test("jmp2.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp2.nasm'))
def test_jmp2_else():
    ram = {0: 0, 1: 5}
    tst = {0: 2}
    assert nasm_test("jmp2.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp3.nasm'))
def test_jmp3_if_equal():
    ram = {0: 0, 1: 1, 2: 2}
    tst = {0: 1}
    assert nasm_test("jmp3.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp3.nasm'))
def test_jmp3_if_gt():
    ram = {0: 0, 1: 2, 2: 2}
    tst = {0: 1}
    assert nasm_test("jmp3.nasm", ram, tst)

@pytest.mark.telemetry_files(source('jmp3.nasm'))
def test_jmp3_else():
    ram = {0: 0, 1: 2, 2: 0}
    tst = {0: 2}
    assert nasm_test("jmp3.nasm", ram, tst)
