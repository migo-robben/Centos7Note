import unreal

### 1.
chair_asset = unreal.load_asset("/Game/StarterContent/Props/SM_Chair.SM_Chair") # class staticMesh object
unreal.log(chair_asset)
print chair_asset.get_name() # SM_Chair
print chair_asset.get_path_name() # /Game/StarterContent/Props/SM_Chair.SM_Chair

# get property
prop = chair_asset.get_editor_property("lod_for_occluder_mesh")
print prop

# set property
chair_asset.set_editor_property("lod_for_occluder_mesh", 1)
prop = chair_asset.get_editor_property("lod_for_occluder_mesh")
print prop