#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>
float findMaxValue(float *array, int size)
{
    float maxValue = array[0];
    // replace this line with a suitable omp pragma
    #pragma omp parallel for
    for (int i = 1; i < size; i++)
    {
        if (array[i] > maxValue)
        {
            maxValue = array[i];
        }
    }
    return maxValue;
}
int main() 
{
    int size = 1000000;
    float* arr1 = (float*)malloc(size * sizeof(float));
    if (arr1 == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }
    // Start the timer
    clock_t start = clock();
    #pragma omp parallel for
    for (int i = 0; i < size; i++) 
    {
        arr1[i] = i + 1;
    }
    float max_value = findMaxValue(arr1, size); 
    // Stop the timer
    clock_t end = clock();
    double cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
    // Printing a few elements as an example
    printf("Max: ");
    printf("%f ", max_value);
    printf("\n");
    printf("Time taken: %f seconds\n", cpu_time_used);
    free(arr1);
    return 0;
}