#include <stdio.h>
#include <limits.h>

int main() {
  /* If our CHAR_BIT is 8 bits wide, we won't mangle UTF.
   */
  printf("%d", CHAR_BIT);
}
