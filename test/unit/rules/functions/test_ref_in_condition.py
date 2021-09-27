"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from test.unit.rules import BaseRuleTestCase
from cfnlint.rules.functions.RefInCondition import RefInCondition  # pylint: disable=E0401


class TestRulesRefInCondition(BaseRuleTestCase):
    """Test Rules Ref exists """

    def setUp(self):
        """Setup"""
        super(TestRulesRefInCondition, self).setUp()
        self.collection.register(RefInCondition())

    def test_file_positive(self):
        """Test Positive"""
        self.helper_file_positive()

    def test_file_negative(self):
        """Test failure"""
        self.helper_file_negative('test/fixtures/templates/bad/functions/ref.yaml', 1)