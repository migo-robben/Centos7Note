import unreal

def log_hello_unreal():
	unreal.log("Hello Unreal")
	unreal.log_warning("Hello Unreal Warning")


def import_skeletal_mesh(fbx_path, game_path, asset_name):
	"""
	Import a single skeletalMesh into the engine provided and FBX.
	:param Path to fbx
	:param Game path asset location
	:param Name of asset
	"""
	# Create an import task.
	import_task = unreal.AssetImportTask()

	# Set base properties on the import task
	import_task.filename         = fbx_path
	import_task.destination_path = game_path
	import_task.destination_name = asset_name
	import_task.automated        = True # Suppress UI.

	# Set the skeletal mesh options on the import task
	import_task.options = _get_skeletal_mesh_import_options()

	# Import the skeletalMesh
	unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])
	importd_assets = import_task.get_editor_property("imported_object_paths")

	if not importd_assets:
		unreal.log_warning("No assets were imported!")
		return

	# Return the instance of the imported SkeletalMesh
	return unreal.load_asset(importd_assets[0])


def _get_skeletal_mesh_import_options():
	options                     = unreal.FbxImportUI()
	options.import_as_skeletal  = True
	options.import_mesh         = True
	options.mesh_type_to_import = unreal.FBXImportType.FBXIT_SKELETAL_MESH

	# Default to compute normals.
	import_method                                          = unreal.FBXNormalImportMethod.FBXNIM_COMPUTE_NORMALS
	options.skeletal_mesh_import_data.normal_import_method = import_method

	# Don't import materials or textures.
	options.import_animations = True
	options.import_materials  = False
	options.import_textures   = False

	return options


def regenerate_skeletal_mesh_lods(skeletal_mesh, number_of_lods=4):
	"""
	Regenerate the LODs to a specific LOD level.
	NOTE: EditorScriptingUtilities plugin needs to be loaded.

	:param SkeletalMesh object
	:param Number of LODs to generate
	"""
	did_update_lods = skeletal_mesh.regenerate_lod(number_of_lods)
	if not did_update_lods:
		unreal.log_warning("Unable to generate LODs for {}".format(skeletal_mesh.get_full_name()))


def set_metadata_tags_on_asset(asset, tags):
	"""
	Sets metadata tags on a given asset
	"""
	for tag in tags:
		unreal.EditorAssetLibrary.set_metadata_tag(asset, tag, tags[tag])
	save_assets(asset)


def get_metadata_tag_on_asset(asset, tag):
	"""
	Get metadata from a given tag on asset
	"""
	return unreal.EditorAssetLibrary.get_metadata_tag(asset, tag)


def get_selected_assets():
	"""
	Get the assets currently selected in the Content Browser.
	"""
	utility_base = unreal.GlobalEditorUtilityBase.get_default_object()
	return utility_base.get_selected_assets()


def save_assets(assets, force_save=False):
	"""
	Saves the given asset objects.
	:param List of asset objects to save.
	"""
	failed_assets    = []
	only_if_is_dirty = not force_save
	assets           = assets if isinstance(assets, list) else [assets]

	for asset in assets:
		asset_path = asset.get_full_name()
		if unreal.EditorAssetLibrary.save_asset(asset_path, only_if_is_dirty):
			unreal.log("Saved newly Created asset: {}".format(asset_path))
		else:
			unreal.log_warning("FAILED TO SAVE newly created asset: {}".format(asset_path))
			failed_assets.append(asset)

	return len(failed_assets) == 0, failed_assets


# Examples
# fbx_path   = r"F:/FBX/Boxing.fbx"
# game_path  = "/Game/Content/Boxing"
# asset_name = "Boxing"
# Boxing_asset = import_skeletal_mesh(fbx_path, game_path, asset_name)

# Regenerate LODs
# regenerate_skeletal_mesh_lods(Boxing_asset)

# set_metadata_tags_on_asset(Boxing_asset, {"Python":"live demo"})
# print get_metadata_tag_on_asset(Boxing_asset, "Python")