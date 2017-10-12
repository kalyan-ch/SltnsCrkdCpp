#include <iostream>

using namespace std;

int main(){

	string word;
	cin >> word;
	int bitvec = 0;
	bool flag = true;

	for (int i = 0; i < word.length(); ++i){
		int index = word[i] - 'a';
		int mask = 1 << index;
		bitvec = bitvec ^ mask;
	}

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