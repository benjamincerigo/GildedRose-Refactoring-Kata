# Next
Some thoughts on the next steps for refactoring.

In general there should an iterative refactoring of legacy updater. In which Item type should be
refactored one by one.

## Side effects
The main interface for updating uses side effects. Meaning that the update doesn't return a new list but updates the old list.

In my experience side effects should be avoided as they make code bases harder to understand and test.

It might then be an idea the update be changed so that it returns a new list of Items.


## ItemDefinition
The side effect of updating `sell_in` property to define the date makes me feel a bit uncomfortable. Firstly because of the case:

- Updates are done on a daily base
- An undetected error in updater is committed and used for a number of days
- The error is then detected and each Item has to then be fixed by hand
- This could be extremely time consuming if the list of items is large


It might then be better to have:

- ItemDeinition list which would look something like:
```
class ItemDefinition:
  id: string
  sell_by_date: date
  sold: bool
  quality_evaluator: id of an quality_evaluator
  created_at:
  updated_at:
```
- Have the date as an optional parameter for `update_items`
- Create a list of Items from the `ItemDefinitions` from the date parameter
- The items would then be a view of the `ItemDefinitions` for a date

In my opinion this would be a better implementation of the domain and would mean that the undetected errors would not be a problem.
On top of this it makes the evaluation of the quality easier to understand for each Item.
