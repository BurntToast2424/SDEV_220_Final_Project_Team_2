import json


seasons = ("winter", "summer", "spring", "fall")

def start_database() -> None:
	data = []
	for season in seasons:
		data.append({"season": season, "items": []})
	save_items(data)

def load_database() -> list[dict[str, str, str]]:
	try:
		with open("database.json", "r") as file:
			data = json.load(file)
	except FileNotFoundError as e:
		print(f"[-] Error: {e}")	
		start_database()
		data = load_database()
	
	return data	

def add_item(season: str, name: str, price: str) -> None:

	if season not in seasons:
		raise Exception("Cant add item not valid season")

	print(f"[+] Adding item in {season} (name={name}) [price={price}]")
	data = load_database()
	print(data)

	item_to_add = {"name": name, "price": price}

	for item in data:
		if season != item.get("season"):
			continue
		item["items"].append(item_to_add)
		break

	save_items(data)
def save_items(db: dict) -> None:
	try:
		with open("database.json", "w") as file:
			json.dump(db, file, indent=4)
	except FileNotFoundError as e:
		print(f"[-] Error {e}")
							
		
if __name__ == '__main__':
	add_item("summer", "summer seeds", "4")
			
