#include <stdio.h>
#include <stdlib.h>

int *merge_sorted_arrays(int *a, int *b, size_t n, size_t m)
{
  int *c = (int *)malloc((n + m) * sizeof(int));
  int *c_head = c;
  n = (size_t)(a + n);
  m = (size_t)(b + m);
  while ((size_t)a < n && (size_t)b < m)
  {
    if (*a < *b)
      *(c++) = *(a++);
    else
      *(c++) = *(b++);
  }
  while ((size_t)a < n)
    *(c++) = *(a++);
  while ((size_t)b < m)
    *(c++) = *(b++);
  return c_head;
}

int main()
{
  int a[] = {1, 3, 5, 7, 9};
  int b[] = {2, 4, 6, 8, 10};
  int *c = merge_sorted_arrays(a, b, 5, 5);

  for (int i = 0; i < 10; i++)
  {
    printf("%d ", c[i]);
  }

  free(c);

  return 0;
}