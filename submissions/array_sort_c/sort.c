#include <stdio.h>
#include <stdlib.h>

int compare(const void * a, const void * b) {
    return (*(int *)a - *(int *)b);
}
 
int main() {
    int size;
    int num;
    printf("Enter the size of the array you want to sort:");
    scanf("%d", &size);
    int * array = malloc(sizeof(int)*size);
    for(int i = 0; i < size; i++) {
        printf("Enter a number:");
        scanf("%d", &num);
        array[i] = num;
    }
    qsort(array, size, sizeof(int), compare);
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    free(array);
    return 0;
}