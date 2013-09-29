//Q.The sum of the squares of the first ten natural numbers is,
//  12 + 22 + ... + 102 = 385
//  The square of the sum of the first ten natural numbers is,
//  (1 + 2 + ... + 10)2 = 552 = 3025
//  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
//  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
// Date: Mar 8,2013
// Author: Shantanu Sarkar
#include<stdio.h>
#include<math.h>
int main()
{
	int i, sum=0,sqsum=0,diff=0;
	for(i=1;i<=100;i++)
		sqsum=sqsum+(pow(i,2));
	for(i=1;i<=100;i++)
		sum=sum+i;
	sum=pow(sum,2);
	diff=sum-sqsum;
	printf("%d",diff);
}
