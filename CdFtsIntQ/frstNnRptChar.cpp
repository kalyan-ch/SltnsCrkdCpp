#include <iostream>

using namespace std;

char firstNotRepeatingCharacter(string s) {
	int buf[26]={0};
	for (int i = 0; i < s.length(); ++i){
	    int num = s[i]-'a';
		buf[num]++;
	}
    int index = s.length();
	for(int i=0;i<26;++i){
		if(buf[i]==1){
			char c = i+97;
		    int pos = s.find(c);
		    if(pos<index){
		    	index = pos;
		    }
		}
	}
	if(index<s.length()){
		return s[index];	
	}else{
		return '_';
	}
	
}

int main(){
	cout<< firstNotRepeatingCharacter("abacbad")<<endl;
}