//Q. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//   Find the sum of all the primes below two million.
// Date: Mar 17, 2013
// Author: Shantanu Sarkar
#include<stdio.h>
long int isprime(long int a)
{
	long int i, count=0;
	for(i=2;i<=a/2;i++)
	{
		if(a%i==0)
		{	count++;
			break;
		}
	}
	if(count==0)
		return (0);
	else
		return(1);
}
long int main()
{	
	long int a,i,s=0;
	for(i=2;i<2000000;i++)
	{
		a=isprime(i);
		if(a==0)
			s=s+i;
		printf("%ld \t %ld\n",i,s);
	}
	printf("%ld",s);
}
