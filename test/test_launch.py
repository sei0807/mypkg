# SPDX-FileCopyrightText: 2025 Seiya Ohata
# SPDX-License-Identifier: BSD-3-Clause

import os
import sys
import unittest
import launch
import launch_ros
import launch_ros.actions
import launch_testing.actions
import pytest


@pytest.mark.launch_test
def generate_test_description():
    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
    )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
    )

    return launch.LaunchDescription([
        talker,
        listener,
        launch_testing.actions.ReadyToTest(),
    ])


class TestTalkerListener(unittest.TestCase):
    def test_exit_code(self, proc_info):
        pass
