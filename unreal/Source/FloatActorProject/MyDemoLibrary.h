// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "MyDemoLibrary.generated.h"

/**
 * 
 */
USTRUCT(BlueprintType)
struct FMyDemoStruct
{
	GENERATED_BODY()

	//UPROPERTY(EditAnywhere)
	UPROPERTY()
	int32 LockCount = 0;
};

UCLASS()
class FLOATACTORPROJECT_API UMyDemoLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:
	/*
	Check to see whether the given struct is currently locked.
	@param InStruct The Struct to test.
	@return True if the struct is locked, false otherwise.
	*/
	UFUNCTION(BlueprintPure, Category = "PythonDemo", meta = (ScriptMethod = "IsLocked"))
	static bool IsStructLocked(const FMyDemoStruct& InStruct);

	/*
	Lock the given struct.
	@param InStruct The struct to lock.
	*/
	UFUNCTION(BlueprintCallable, Category = "PythonDemo", meta = (ScriptMethod = "Lock"))
	static void LockStruct(UPARAM(ref) FMyDemoStruct& InStruct);

	/*
	Unlock the given struct.
	@param InStruct The struct to unlock.
	*/
	UFUNCTION(BlueprintCallable, Category = "PythonDemo", meta = (ScriptMethod = "Unlock"))
	static void UnlockStruct(UPARAM(ref) FMyDemoStruct& InStruct);
};

/* Python Example - for struct EditAnywhere:
s = unreal.MyDemoStruct()
print s.get_editor_property("lock_count")

print unreal.MyDemoLibrary.is_struct_locked(s)
s = unreal.MyDemoLibrary.lock_struct(s)

print unreal.MyDemoLibrary.is_struct_locked(s)
print s.get_editor_property("lock_count")
s = unreal.MyDemoLibrary.unlock_struct(s)


Python Example - for not struct EditAnywhere
s = unreal.MyDemoStruct()
print s.is_locked()
s.lock()
s.unlock()
*/