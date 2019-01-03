#include <stdio.h>

int main()

{

      float a, b, c;

      printf("\nPlease enter 3 numbers: ");

      scanf("%f %f %f", &a, &b, &c);

      if(a<=b && a<=c)

         printf("The smallest number is %.3f", a);

      if(b<=a && b<=c)

         printf("The smallest number is %.3f", b);

      if(c<=a && c<=b)

         printf("The smallest number is %.3f", c);

      return 0;

}
