import unittest

import sieve.extension
import sieve.grammar


class TestEvaluationState(unittest.TestCase):

    def setUp(self):
        sieve.extension.register('ext1')
        sieve.extension.register('ext2')
        self.state = sieve.grammar.EvaluationState()

    def test_require_extension(self):
        self.state.require_extension('ext1')
        self.assertTrue(self.state.check_required_extension('ext1', 'ext1'))
        self.assertRaises(
                RuntimeError,
                self.state.check_required_extension,
                'ext2', 'ext2',
            )


if __name__ == '__main__':
    unittest.main()
