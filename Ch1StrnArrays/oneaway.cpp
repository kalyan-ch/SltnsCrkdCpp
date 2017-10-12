#include <iostream>
#include <cmath>

using namespace std;

bool oneEditAway(string *first, string *second){
	int i = 0;
    int j = 0;
    string s1 = (first->length() < second->length())?*first:*second;
    string s2 = (first->length() < second->length())?*second:*first;
    int count=0;
    while(i<s1.length() && j<s1.length()){
    	if(s1[i] != s2[j]){
    		count++;
    		if(count>1){
    			return false;
    		}

    		if(s1.length()==s2.length()){
    			i++;
    		}
    	}else{
    		i++;
    	}

    	j++;
    }
    return true;
}

int main(){

	string word1, word2;
	cin >> word1;
	cin >> word2;
	bool flag = true;
	int diff = abs(word1.length() - word2.length());

	if (diff > 1){
		flag = false;
	}else{
		flag = oneEditAway(&word1, &word2);
	}

	if(flag){
		cout << "yes! one(or zero) edit away!";
	}else{
		cout << "no! not one edit away!";
	}

}
