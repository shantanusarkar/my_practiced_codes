//Q. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// Date: Mar 8,2013
// Author: Shantanu Sarkar

#include<stdio.h>
int main()
{
	int i,j,prod;
	for(i=1;i<100000000000000000;i++)
	{
		if(i%9==0 && i%11==0 && i%13==0 && i%14==0 && i%15==0 && i%16==0 && i%17==0 && i%18==0 && i%19==0 && i%20==0)
		{
			printf("%d",i);
			break;
		}
	}
}
