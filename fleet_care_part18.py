# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: FleetCare
def add_tag(vehicle_id: str, tag_name: str) -> dict:
    """Добавить тег к автомобилю."""
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        return {"error": "Vehicle not found"}
    tags = vehicle.get("tags", [])
    if any(t["name"].lower() == tag_name.lower() for t in tags):
        return {"error": "Tag already exists"}
    new_tag = {"id": generate_id(), "name": tag_name, "added_date": date()}
    tags.append(new_tag)
    vehicle["tags"] = tags
    save_data(DATA_FILE)
    return {"success": True, "tag": new_tag}


def remove_tag(vehicle_id: str, tag_id: str) -> dict:
    """Удалить тег у автомобиля."""
    vehicle = find_vehicle(vehicle_id)
    if not vehicle:
        return {"error": "Vehicle not found"}
    tags = vehicle.get("tags", [])
    for i, t in enumerate(tags):
        if t["id"] == tag_id:
            tags.pop(i)
            vehicle["tags"] = tags
            save_data(DATA_FILE)
            return {"success": True, "removed_tag": t}
    return {"error": "Tag not found"}
