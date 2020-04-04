#include <stdio.h>
#include <stdint.h>

/* Printing big numbers is hard to remember. */
int main() {
    /* We can use %lld and %llu to print long long numbers in decimal. */
    printf("long long decimal (pos): %lld\n", 9223372036854775807ll);
    printf("long long decimal (neg):%lld\n", -9223372036854775807ll);
    printf("unsigned long long: %llu\n", 18446744073709551615ull);
    return 0;
}
