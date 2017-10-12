#ifndef __NODE_H_INCLUDED__
#define __NODE_H_INCLUDED__
#endif

class Node
{
		
	public:
		int data;
		Node* next;
		Node(int val){
			data = val;
			next = NULL;
		}

		int getVal(){
			return data;
		}
	
};