//Q. A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//   a2 + b2 = c2
//   For example, 32 + 42 = 9 + 16 = 25 = 52.
//   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//   Find the product abc.
// Date: Mar 16, 2013
// Author: Shantanu Sarkar

#include<stdio.h>
int main()
{
	int a,b,c,s=1,s1=0,s2=0,s3=0;
	for(a=1;a<=1000;a++)
	{
		for(b=1;b<a;b++)
		{
			for(c=1;c<b;c++)
			{
				s1=a*a;
				s2=b*b;
				s3=c*c;
				if(s1==(s3+s2))
				{
					if(a+b+c ==1000)
					{
						printf("%d \t %d \t %d",a,b,c);
					}
				}
			}
		}
	}
	printf("%d",s);
	return 0;
}
