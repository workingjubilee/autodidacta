#include <stdint.h>
#include <stdio.h>

int main() {
  /* GCC will try to warn if you do this explicitly.
     The type may be uint64_t but it overflows somehow. What gives?
  */
  uint64_t overflow = 1 << 33;
  printf("%lld\n", overflow);

  /*  This is because C defaults to 32-bit signed ints in bitshifts,
      and even though you've marked the type as uint64_t,
      that is not set until assignment is done!
      Instead, mark it using integer literal syntax.
   */
  uint64_t literal_bignum = 1ull << 33;
  printf("%lld\n", literal_bignum);

  /*  Alternately, we can complete assignment of our initial number,
   *  then do a bitshift on it.
   */
  uint64_t assigned_bignum = 1;
  assigned_bignum <<= 33;
}
