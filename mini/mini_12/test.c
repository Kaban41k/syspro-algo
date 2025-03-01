#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARR_N 10000000
#define MAX_ELEM 100000

int* random_arr(size_t size){
  int* arr = malloc(size * sizeof(int));

  for(size_t i = 0; i < size; ++i)
    arr[i] = rand() % MAX_ELEM;
  return arr;
}

int* copy_arr(int* arr, size_t size) {
  int* copy = malloc(size * sizeof(int));
  
  for (size_t i = 0; i < size; i++) {
    copy[i] = arr[i];
  }

  return copy;
}

void swap(int* a, int* b) {
  if (a == b)
    return;

  int c = *a;
  *a = *b;
  *b = c;
}

void mod_lomuto_sort(int* arr, size_t size) {
  if (size <= 1)
    return;

  if (size == 2) {
    if (arr[0] > arr[1])
      swap(arr, arr + 1);
    return;
  }

  int randi = rand() % size;
  int pivot = arr[randi];
  swap(arr, arr + randi);

  int* l = arr;
  int* h = arr + 1;
  int* c = arr + 1;

  while (c < arr + size) {
    if (*c < pivot) {
      int tmp = *c;
      *c = *h;
      *h = *l;
      *l = tmp;
      l++;
      h++;
      c++;
    } else if (*c == pivot) {
      swap(h, c);
      h++;
      c++;
    } else if (*c > pivot) 
      c++;
  }

  mod_lomuto_sort(arr, l - arr);
  mod_lomuto_sort(h, c - h);
}


void hoar_sort(int* arr, size_t size) {
  if (size <= 1)
    return;

  if (size == 2) {
    if (arr[0] > arr[1])
      swap(arr, arr + 1);
    return;
  }

  int randi = rand() % size;
  int pivot = arr[randi];

  int* i = arr;
  int* j = arr + size - 1;

  while (i <= j) {
    if (*i < pivot) i++;
    else if (*j > pivot) j--;
    else if (*i >= pivot && *j <= pivot) {
      swap(i, j);
      i++;
      j--;
    }
  }

  hoar_sort(arr, i - arr);
  hoar_sort(i, arr + size - i);

  return;
}

int* lomuto_partition_branchfree(int* first, int* last) {
    if (last - first < 2)
        return first; // nothing interesting to do
    // Choose pivot.
    --last;
    if (*first > *last)
        swap(first, last);
    int* pivot_pos = first;
    int pivot = *first;
    // Prelude.
    do {
        ++first;
    } while (*first < pivot);
    // Main loop.
    for (int* read = first + 1; read < last; ++read) {
        int x = *read;
        int less = -(int)(x < pivot);
        int delta = less & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= less;
    }
    // Move the pivot to its final slot.
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}

void lomuto_partition_branchfree_sort(int* arr, size_t size) {
  if (size <= 1)
    return;

  if (size == 2) {
    if (arr[0] > arr[1])
      swap(arr, arr + 1);
    return;
  }

  int* center = lomuto_partition_branchfree(arr, arr + size);

  lomuto_partition_branchfree_sort(arr, center - arr + 1);
  lomuto_partition_branchfree_sort(center + 1, arr + size - center - 1);
}


void lomuto_sort(int* arr, int size) {
  if (size <= 1)
    return;

  if (size == 2) {
    if (arr[0] > arr[1])
      swap(arr, arr + 1);
    return;
  }

  int randi = rand() % size;
  int pivot = arr[randi];
  swap(arr, arr + randi);

  int* i = arr + 1;
  int* j = arr + 1;

  while (j < arr + size) {
    if (*j <= pivot) {
      swap(i, j);
      i++;
    }

    j++;
  }
  
  swap(arr, i - 1);

  lomuto_sort(arr, i - arr - 1);
  lomuto_sort(i, j - i);


  return;
}

int main() {
  int* arr = random_arr(ARR_N);
  int* copy1 = copy_arr(arr, ARR_N);
  int* copy2 = copy_arr(arr, ARR_N);
  int* copy3 = copy_arr(arr, ARR_N);
  
  clock_t start, end;
  double time;

  start = clock();
  lomuto_sort(arr, ARR_N);
  end = clock();
  time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("classic Lomuto: %.6f sec\n", time);

  start = clock();
  mod_lomuto_sort(copy1, ARR_N);
  end = clock();
  time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Mod Lomuto: %.6f sec\n", time);

  start = clock();
  lomuto_partition_branchfree_sort(copy3, ARR_N);
  end = clock();
  time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Mega cool Lomuto: %.6f sec\n", time);

  start = clock();
  hoar_sort(copy2, ARR_N);
  end = clock();
  time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Hoar: %.6f sec\n", time);

  free(arr);
  free(copy1);
  free(copy2);
  free(copy3);

  return 0;
}