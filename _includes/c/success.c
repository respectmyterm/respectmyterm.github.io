#include <stdarg.h>
#include <stdio.h>
#include <term.h>

void success(const char *fmt, ...) {
    va_list argp;
    char *colors = tigetstr("setaf");

    if (colors)
        printf("%s", tparm(colors, 2));
    va_start(argp, fmt);
    vprintf(fmt, argp);
    va_end(argp);
    if (colors)
        printf("%s", tparm(colors, 0));
}

int main() {
    setupterm(NULL, 1, 0);
    success("Hello, World!\n");
    return 0;
}
