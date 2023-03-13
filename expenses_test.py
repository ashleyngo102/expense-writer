import unittest

from expenses import *


class Expenses_Test(unittest.TestCase):

    def setUp(self):
        """The setUp function runs before every test function."""

        # create expenses dictionary and populate with data
        self.expenses = {'food': 5.0, 'coffee': 12.4, 'rent': 825.0, 'clothes': 45.0,
                         'entertainment': 135.62, 'music': 324.0, 'family': 32.45}

    def test_import_expenses(self):
        # import expenses files
        expenses = {}
        import_expenses(expenses, 'expenses.txt')
        import_expenses(expenses, 'expenses_2.txt')

        # test existing total expenses
        self.assertAlmostEqual(45, expenses['clothes'])
        self.assertAlmostEqual(12.40, expenses['coffee'])
        self.assertAlmostEqual(135.62, expenses['entertainment'])
        
    def test_get_expense(self):
        # test getting expenses based on expense type
        self.assertAlmostEqual(12.40, get_expense(self.expenses, "coffee"))

        # test non-existing expense types
        self.assertEqual(None, get_expense(self.expenses, "phone"))

        # TODO insert 2 additional test cases
        #  Hint(s): Test both existing and non-existing expense types
        # edge case
        self.assertEqual(None,get_expense(self.expenses,""))
        self.assertEqual(None,get_expense(self.expenses,"cloth"))
        self.assertEqual(None, get_expense(self.expenses, "subscription"))
    def test_add_expense(self):
        # test adding a new expense
        add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios"))

        # TODO insert 2 additional test cases
        #  Hint(s): Test adding to existing expenses
        add_expense(self.expenses,"rent",30)
        self.assertAlmostEqual(855.0,self.expenses.get("rent"))

        #add negative expense amount
        add_expense(self.expenses,"food",-2)
        self.assertAlmostEqual(5,self.expenses.get("food"))
        #print("food",self.expenses["food"])

        #enter non-numeric value
        add_expense(self.expenses,"clothes","shirt")
        self.assertAlmostEqual(45,self.expenses.get("clothes"))

    def test_deduct_expense(self):
        # test deducting from expense
        deduct_expense(self.expenses, "coffee", .99)
        self.assertAlmostEqual(11.41, self.expenses.get("coffee"))

        # test deducting from expense
        deduct_expense(self.expenses, "entertainment", 100)
        self.assertAlmostEqual(35.62, self.expenses.get("entertainment"))

        # TODO insert 2 additional test cases
        #  Hint(s):
        #   Test deducting too much from expense
        self.assertRaises(RuntimeError,deduct_expense,self.expenses,"family",55)
        #   Test deducting from non-existing expense
        deduct_expense(self.expenses,"subscription",10)
        self.assertEqual(None,self.expenses.get("subscription"))
        #enter non-numeric value
        deduct_expense(self.expenses,"rent","flat")
        self.assertAlmostEqual(825,self.expenses.get("rent"))
        #enter negative amount
        deduct_expense(self.expenses,"rent",-200)
        self.assertAlmostEqual(825.0,self.expenses.get("rent"))

    def test_update_expense(self):
        # test updating an expense
        update_expense(self.expenses, "clothes", 19.99)
        self.assertAlmostEqual(19.99, get_expense(self.expenses, "clothes"))

        # TODO insert 2 additional test cases
        #  Hint(s):
        #   Test updating an expense
        update_expense(self.expenses,"rent",0)
        self.assertAlmostEqual(0,get_expense(self.expenses,"rent"))
        # update a negative number
        update_expense(self.expenses, "family", -100)
        self.assertAlmostEqual(32.45, get_expense(self.expenses, "family"))
        #   Test updating a non-existing expense
        update_expense(self.expenses,"sport",279.5)
        self.assertEqual(None,get_expense(self.expenses,"sport"))

    def test_sort_expenses(self):
        # test sorting expenses by 'expense_type'
        expense_type_sorted_expenses = [('clothes', 45.0),
                                        ('coffee', 12.40),
                                        ('entertainment', 135.62),
                                        ('family', 32.45),
                                        ('food', 5.0),
                                        ('music', 324.0),
                                        ('rent', 825.0)]

        self.assertListEqual(expense_type_sorted_expenses, sort_expenses(self.expenses, "expense_type"))

        # TODO insert 1 additional test case
        #   Hint: Test sorting expenses by 'amount'
        amount_sorted_expenses = [('rent',825.0),
                                  ('music', 324.0),
                                  ('entertainment', 135.62),
                                  ('clothes', 45.0),
                                  ('family', 32.45),
                                  ('coffee', 12.40),
                                  ('food', 5.0)]
        self.assertListEqual(amount_sorted_expenses,sort_expenses(self.expenses,"amount"))

    def test_export_expenses(self):
        #  Note: Unless you add assert() statements or there is an exception, this test will pass regardless of the
        #  correctness of your export_expenses() function, so passing this test is not a guarantee of correctness.

        # test export with existing expense types.
        # this will create a new file called “export1.txt” that you should visually inspect for correctness
        export_expenses(self.expenses, ['coffee', 'clothes'], 'export1.txt')

        # TODO insert 1 additional test case
        #   Hint: Test exporting with some non-existent expense types.
        #   Similar to above, it is acceptable to just call export_expenses() using different inputs with a different
        #   file to write to and just visually inspect the results. You are not required to have any assert() statements
        #   in this test function.
        export_expenses(self.expenses,['subscription','family'],'test1.txt')

if __name__ == '__main__':
    unittest.main()
