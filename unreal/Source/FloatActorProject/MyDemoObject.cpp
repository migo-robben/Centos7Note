// Fill out your copyright notice in the Description page of Project Settings.


#include "MyDemoObject.h"

bool UMyDemoObject::MyFunction(const int32 InValue) {
	return InValue > 0;
}

int32 UMyDemoObject::MyPureFunction() const {
	return PureTest;
}