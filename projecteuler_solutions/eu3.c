//Q. The prime factors of 13195 are 5, 7, 13 and 29.
//   What is the largest prime factor of the number 600851475143 ?
//Date: Mar 8,2013
//Author: Shantanu Sarkar
#include<stdio.h>
long int isprime(long int a)
{
	long int i, count=0;
	for(i=1;i<=a;i++)
	{
		if(a%i==0)
			count++;
	}
	if(count==2)
		return (0);
	else
		return(1);
}
long int main()
{
	long int num,grt=1,fac,i,j;
	printf("Enter a number :");
	scanf("%ld",&num);
	for(i=1;i<=num;i++)
	{
		if(num%i==0)
		{
			fac=i;
			j=isprime(fac);
			if(j==0&&grt<fac)
				grt=fac;
		}
	}
	printf("%ld",grt);
}		
