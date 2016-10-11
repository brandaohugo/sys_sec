#include <stdio.h>


int get_cookie() {
	return 0x41424343;
}

int main() {
	int guess;
	char name[20];

	guess = get_cookie();
	printf("Enter your name: ");
	fgets(name, 20, stdin);
	

	if(guess == 0x41424344) {
		printf("You win");
	} else {
		printf("Better luck next time %s : (\n" , name);
	}
}