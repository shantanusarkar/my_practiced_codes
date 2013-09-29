//Q. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//   What is the 10 001st prime number?
// Date: Mar 15, 2013
// Author: Shantanu Sarkar
#include<stdio.h>
long int isprime(long int a)
{
	long int v, count=0;
	for(v=2;v<=a/2;v++)
	{
		if(a%v==0)
		{
			count++;
			break;
			
		}
	}
	if(count==1)
		return (0);
	else
		return(1);
}
long int main()
{
	long int j=2,k=2,s,count1=0;
	while(k<=10001)
	{
		j++;
		count1=isprime(j);
		if(count1==1)
		{
			s=j;
			k++;
		}
		
	}
	printf(" %ld",j);
}
