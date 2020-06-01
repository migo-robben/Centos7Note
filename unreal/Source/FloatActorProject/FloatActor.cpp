// Fill out your copyright notice in the Description page of Project Settings.

#include "FloatActor.h"

// Sets default values
AFloatActor::AFloatActor()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	VisualMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Mesh"));

	static ConstructorHelpers::FObjectFinder<UStaticMesh> customAsset(TEXT("/Game/MyStaticMeshes/MyObject.MyObject"));

	//// Create or load asset
	//if (customAsset.Succeeded())
	//{	
	//	// Load Asset
	//	UE_LOG(LogTemp, Log, TEXT("Already created asset: MyObject"));
	//	VisualMesh->SetStaticMesh(customAsset.Object);
	//	VisualMesh->SetRelativeLocation(FVector(0.0f, 0.0f, 0.0f));
	//}

	//else {
	//	// Create Asset
	//	UE_LOG(LogTemp, Log, TEXT("Start create asset: MyObject"));
	//	CreateStaticMesh();
	//	VisualMesh->SetStaticMesh(StaticMesh);
	//	VisualMesh->SetRelativeLocation(FVector(0.0f, 0.0f, 0.0f));
	//}

	CreateStaticMesh_Description();

	//TArray<int32> test{ 1, 2, 3 };
	//UE_LOG(LogTemp, Log, TEXT("Array: %d"), test[0]);
}

void AFloatActor::CreateStaticMesh() {
	// Object Details
	FString AssetName = TEXT("MyObject");
	FString MountPath = TEXT("/Game/MyStaticMeshes/");
	FString AssetPath = TEXT("/Game/MyStaticMeshes/") + AssetName;
	FString AbsolutePathPackage = FPaths::EngineContentDir() + "/MyStaticMeshes";

	FPackageName::RegisterMountPoint(*MountPath, *AbsolutePathPackage);
	UPackage* NewMeshPack = CreatePackage(nullptr, *AssetPath);

	// Create Static Mesh
	StaticMesh = NewObject<UStaticMesh>(NewMeshPack, FName(*AssetName), RF_Public | RF_Standalone);
	
	TArray<FVector> Vertices;
	Vertices.Add(FVector(86.6, 75, 0));
	Vertices.Add(FVector(-86.6, 75, 0));
	Vertices.Add(FVector(2.13, 25, 175));
	Vertices.Add(FVector(2.13, -75, 0));
	int numberOfVertices = Vertices.Num();

	struct Face {
		unsigned int v1;
		unsigned int v2;
		unsigned int v3;
		short materialID;
		FVector2D uvCoords1;
		FVector2D uvCoords2;
		FVector2D uvCoords3;
	};
	TArray<Face> Faces;
	Face oneFace;
	oneFace = { 1,3,0,  0,  FVector2D(0,0), FVector2D(1, 0), FVector2D(0.5, 1) };
	Faces.Add(oneFace);
	oneFace = { 0,2,1,  1,  FVector2D(0,0), FVector2D(1, 0), FVector2D(0.5, 1) };
	Faces.Add(oneFace);
	oneFace = { 3,2,0,  0,  FVector2D(0,0), FVector2D(1, 0), FVector2D(0.5, 1) };
	Faces.Add(oneFace);
	oneFace = { 1,2,3,  1,  FVector2D(0,0), FVector2D(1, 0), FVector2D(0.5, 1) };
	Faces.Add(oneFace);
	int numberOfFaces = Faces.Num();

	TArray<FStaticMaterial> Materials; // This should contain the real Materials, this is just an example
	Materials.Add(FStaticMaterial());
	Materials.Add(FStaticMaterial());
	int numberOfMaterials = Materials.Num();

	if (StaticMesh != NULL)
	{
		FRawMesh myRawMesh  = FRawMesh();
		FColor WhiteVertex  = FColor(255, 255, 255, 255);
		FVector EmptyVector = FVector(0, 0, 0);

		// Vertices
		for (int vertIndex = 0; vertIndex < numberOfVertices; vertIndex++) {
			myRawMesh.VertexPositions.Add(Vertices[vertIndex]);
		}

		// Faces and UV/Normals
		for (int faceIndex = 0; faceIndex < numberOfFaces; faceIndex++) {
			myRawMesh.WedgeIndices.Add(Faces[faceIndex].v1);
			myRawMesh.WedgeIndices.Add(Faces[faceIndex].v2);
			myRawMesh.WedgeIndices.Add(Faces[faceIndex].v3);

			myRawMesh.WedgeColors.Add(WhiteVertex);
			myRawMesh.WedgeColors.Add(WhiteVertex);
			myRawMesh.WedgeColors.Add(WhiteVertex);

			myRawMesh.WedgeTangentX.Add(EmptyVector);
			myRawMesh.WedgeTangentX.Add(EmptyVector);
			myRawMesh.WedgeTangentX.Add(EmptyVector);

			myRawMesh.WedgeTangentY.Add(EmptyVector);
			myRawMesh.WedgeTangentY.Add(EmptyVector);
			myRawMesh.WedgeTangentY.Add(EmptyVector);

			myRawMesh.WedgeTangentZ.Add(EmptyVector);
			myRawMesh.WedgeTangentZ.Add(EmptyVector);
			myRawMesh.WedgeTangentZ.Add(EmptyVector);

			// Materials
			myRawMesh.FaceMaterialIndices.Add(Faces[faceIndex].materialID);
			myRawMesh.FaceSmoothingMasks.Add(0xFFFFFFFF); // Phong

			for (int UVIndex = 0; UVIndex < MAX_MESH_TEXTURE_COORDS; UVIndex++)
			{
				myRawMesh.WedgeTexCoords[UVIndex].Add(Faces[faceIndex].uvCoords1);
				myRawMesh.WedgeTexCoords[UVIndex].Add(Faces[faceIndex].uvCoords2);
				myRawMesh.WedgeTexCoords[UVIndex].Add(Faces[faceIndex].uvCoords3);
			}
		}

		// Saving mesh in the StaticMesh.
		int32 LODIndex = 0;
		if (!StaticMesh->IsSourceModelValid(LODIndex))
		{
			// Add one LOD 
			StaticMesh->AddSourceModel();
		}
		FStaticMeshSourceModel& SrcModel = StaticMesh->GetSourceModel(LODIndex);
		SrcModel.RawMeshBulkData->SaveRawMesh(myRawMesh);

		// Model Configuration
		SrcModel.BuildSettings.bRecomputeNormals = true;
		SrcModel.BuildSettings.bRecomputeTangents = true;
		SrcModel.BuildSettings.bUseMikkTSpace = false;
		SrcModel.BuildSettings.bGenerateLightmapUVs = true;
		SrcModel.BuildSettings.bBuildAdjacencyBuffer = false;
		SrcModel.BuildSettings.bBuildReversedIndexBuffer = false;
		SrcModel.BuildSettings.bUseFullPrecisionUVs = false;
		SrcModel.BuildSettings.bUseHighPrecisionTangentBasis = false;

		// Assign the Materials to the Slots (optional
		for (int32 MaterialID = 0; MaterialID < numberOfMaterials; MaterialID++) {
			StaticMesh->StaticMaterials.Add(Materials[MaterialID]);
			FMeshSectionInfoMap sectionInfoMap = StaticMesh->GetSectionInfoMap();
			sectionInfoMap.Set(0, MaterialID, FMeshSectionInfo(MaterialID));
		}

		// Processing the StaticMesh and Marking it as not saved
		StaticMesh->ImportVersion = EImportStaticMeshVersion::LastVersion;
		StaticMesh->CreateBodySetup();
		StaticMesh->SetLightingGuid();
		StaticMesh->PostEditChange();
		NewMeshPack->MarkPackageDirty();
		
		// UPackage::SavePackage(NewMeshPack, nullptr, EObjectFlags::RF_Public | EObjectFlags::RF_Standalone, *AssetPath);
		// FAssetRegistryModule::AssetCreated(NewMeshPack->GetOuter());

		UE_LOG(LogTemp, Log, TEXT("Static Mesh created: %s"), *AssetName);
	}
}

void AFloatActor::CreateStaticMesh_Description() {

	// StaticMesh = nullptr;

	// Object Details
	FString AssetName = TEXT("StaticMesh");
	FString MountPath = TEXT("/Game/MyStaticMeshes/");
	FString AssetPath = TEXT("/Game/MyStaticMeshes/") + AssetName;
	FString AbsolutePathPackage = FPaths::EngineContentDir() + "/MyStaticMeshes";

	FPackageName::RegisterMountPoint(*MountPath, *AbsolutePathPackage);
	UPackage* NewMeshPack = CreatePackage(nullptr, *AssetPath);

	// Create Static Mesh
	StaticMesh = NewObject<UStaticMesh>(NewMeshPack, FName(*AssetName), RF_Public | RF_Standalone);

	// Saving mesh in the StaticMesh.
	int32 LODIndex = 0;
	if (!StaticMesh->IsSourceModelValid(LODIndex))
	{
		// Add one LOD 
		StaticMesh->AddSourceModel();
	}

	// Description
	FMeshDescription* MeshDescription = StaticMesh->CreateMeshDescription(LODIndex);
	
	const int32 VertexOffset = MeshDescription->Vertices().Num();
	const int32 VertexInstanceOffset = MeshDescription->VertexInstances().Num();
	const int32 PolygonOffset = MeshDescription->Polygons().Num();

	FStaticMeshAttributes StaticMeshAttributes(*MeshDescription);

	// Vertex positions
	TVertexAttributesRef< FVector > MeshDescriptionVertexPositions = StaticMeshAttributes.GetVertexPositions();
	{
		TArray<FVector> Vertices;
		Vertices.Add(FVector(86.6, 75, 0));
		Vertices.Add(FVector(-86.6, 75, 0));
		Vertices.Add(FVector(2.13, 25, 175));
		Vertices.Add(FVector(2.13, -75, 0));
		int numberOfVertices = Vertices.Num();

		MeshDescription->ReserveNewVertices(numberOfVertices);
		for (int32 LocalPointIndex = 0; LocalPointIndex < numberOfVertices; ++LocalPointIndex) {
			FVertexID AddedVertexId = MeshDescription->CreateVertex();
			MeshDescriptionVertexPositions[AddedVertexId] = Vertices[LocalPointIndex];
		}
	}

	// Polygons
	{	
		TArray<int32> FaceCounts{ 3, 3, 3, 3 };
		TArray<int32> FaceIndices{ 1, 3, 0, 0, 2, 1, 3, 2, 0, 1, 2, 3 };

		TArray<FVertexInstanceID> CornerInstanceIDs;
		TArray<FVertexID> CornerVerticesIDs;
		int32 CurrentVertexInstanceIndex = 0;

		MeshDescription->ReserveNewVertexInstances(FaceCounts.Num() * 3);
		MeshDescription->ReserveNewPolygons(FaceCounts.Num());
		MeshDescription->ReserveNewEdges(FaceCounts.Num() * 2);

		for (int32 PolygonIndex = 0; PolygonIndex < FaceCounts.Num(); ++PolygonIndex) {

			//UE_LOG(LogTemp, Log, TEXT("PolygonIndex: %d"), PolygonIndex);

			int32 PolygonVertexCount = FaceCounts[PolygonIndex];
			CornerInstanceIDs.Reset(PolygonVertexCount);
			CornerVerticesIDs.Reset(PolygonVertexCount);

			for (int32 CornerIndex = 0; CornerIndex < PolygonVertexCount; ++CornerIndex, ++CurrentVertexInstanceIndex)
			{	
				//UE_LOG(LogTemp, Log, TEXT("CornerIndex: %d"), CornerIndex);

				int32 VertexInstanceIndex = VertexInstanceOffset + CurrentVertexInstanceIndex;
				const FVertexInstanceID VertexInstanceID(VertexInstanceIndex);
				const int32 ControlPointIndex = FaceIndices[CurrentVertexInstanceIndex];
				const FVertexID VertexID(VertexOffset + ControlPointIndex);
				const FVector VertexPosition = MeshDescriptionVertexPositions[VertexID];

				if (CornerVerticesIDs.Contains(VertexID))
				{
					//UE_LOG(LogTemp, Log, TEXT("currentVertexInstanceIndex: %d"), CurrentVertexInstanceIndex);
					continue;
				}

				CornerVerticesIDs.Add(VertexID);

				FVertexInstanceID AddedVertexInstanceId = MeshDescription->CreateVertexInstance(VertexID);
				CornerInstanceIDs.Add(AddedVertexInstanceId);
			}

			FPolygonGroupID NewPolygonGroup = MeshDescription->CreatePolygonGroup();
			const FPolygonID NewPolygonID = MeshDescription->CreatePolygon(NewPolygonGroup, CornerInstanceIDs);
		}
	}

	StaticMesh->CommitMeshDescription(LODIndex);
	FStaticMeshSourceModel& SrcModel = StaticMesh->GetSourceModel(LODIndex);
	SrcModel.BuildSettings.bRecomputeNormals = true;
	SrcModel.BuildSettings.bRecomputeTangents = true;
	SrcModel.BuildSettings.bUseMikkTSpace = false;
	SrcModel.BuildSettings.bGenerateLightmapUVs = true;
	SrcModel.BuildSettings.bBuildAdjacencyBuffer = false;
	SrcModel.BuildSettings.bBuildReversedIndexBuffer = false;
	SrcModel.BuildSettings.bUseFullPrecisionUVs = false;
	SrcModel.BuildSettings.bUseHighPrecisionTangentBasis = false;

	StaticMesh->CreateBodySetup();
	StaticMesh->SetLightingGuid();
	StaticMesh->PostEditChange();
	NewMeshPack->MarkPackageDirty();
}

// Called when the game starts or when spawned
void AFloatActor::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AFloatActor::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	FVector  NewLocation = GetActorLocation();
	FRotator NewRotation = GetActorRotation();
	FVector  NewScale = GetActorScale3D();

	float RunningTime = GetGameTimeSinceCreation();
	float DeltaHeight = (FMath::Sin(RunningTime + DeltaTime) - FMath::Sin(RunningTime));

	NewLocation.Z += DeltaHeight * 20.0f;       //Scale our height by a factor of 20
	float DeltaRotation = DeltaTime * 20.0f;    //Rotate by 20 degrees per second
	NewRotation.Yaw += DeltaRotation;
	SetActorLocationAndRotation(NewLocation, NewRotation);

	NewScale.Z = (FMath::Sin(RunningTime)) + 1.5;
	SetActorScale3D(NewScale);
}

