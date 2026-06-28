#include <string.h>
#include <stdbool.h>

bool copy_name(char *dest, size_t dest_size, const char *src, size_t src_len)
{
    if (!dest || !src || dest_size == 0 || src_len >= dest_size) {
        return false;
    }

    memcpy(dest, src, src_len);
    dest[src_len] = '\0';
    return true;
}
