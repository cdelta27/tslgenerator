# Length
  Length:
    0. [error] # do not generate more than one test frame that includes this option. NOT logic error. represents something you only want to test one of and is erroneous input
    # single would be something you only want to test one of but is a valid input
    7.
    8.
    20.
    21.
# Number
  Number:
    None. [error] # if there are no nums, only want to test it once
    One.
    Many.
# Uppercase
  Uppercase:
    None. [property no_upper] #[error]
    One.
    Many.
# Lowercase
  Lowercase:
    None. [if !no_upper] [property no_lower] # [error]
    One.
    Many.
# Symbol
  Symbol:
    None. [error]
    One.
    Many.