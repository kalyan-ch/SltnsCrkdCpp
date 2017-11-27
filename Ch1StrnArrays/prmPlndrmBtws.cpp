#include <iostream>

using namespace std;

int main(){

	string word;
	cin >> word;
	int bitvec = 0;
	bool flag = true;
	// this is essentially counting number of characters in the string. setting the bits to zero means that the character appears even number of time. 1 means odd.
	for (int i = 0; i < word.length(); ++i){
		int index = word[i] - 'a';
		int mask = 1 << index;
		bitvec = bitvec ^ mask;
	}

	// if number of characters is even then the bitvec should be zero for the string to be a palindrom. Odd then only one bit should be set to 1 in the bitvec
	if(word.length()%2==0){
		if(bitvec!=0){
			flag = false;
		}
	}else{
		if(bitvec & (bitvec-1) != 0){
			flag = false;
		}
	}

	cout << "Any permutations a palindrome? "<<flag;

}