
```elixir
ELIXIR CHEATSHEET

def ModuleName do

  @moduledoc """
  documentation for this module
  """

  @doc """
  documentation for next function
  """
  # COMMENT: type signature for next function
  @spec function_name(param_type) :: return_type
  def function_name(params) do
    # Implicit return, next line is return val for function
    result = "Something."
  end # of function

end # of module
```