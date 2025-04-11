import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import random

# File path constants
GAME_DATA_FILE = "sustainability_game_data.json"
ACHIEVEMENTS_FILE = "sustainability_achievements.json"

# Resource types
RESOURCE_TYPES = [
    "Water", 
    "Energy", 
    "Food", 
    "Materials", 
    "Labor"
]

# Building types with costs and benefits
BUILDINGS = {
    "Solar Farm": {
        "cost": {"Materials": 30, "Labor": 20},
        "produces": {"Energy": 10},
        "description": "Produces clean energy from the sun."
    },
    "Wind Turbine": {
        "cost": {"Materials": 25, "Labor": 15},
        "produces": {"Energy": 8},
        "description": "Harnesses wind power for energy production."
    },
    "Community Garden": {
        "cost": {"Water": 10, "Labor": 10, "Materials": 5},
        "produces": {"Food": 10},
        "description": "Provides fresh vegetables and brings the community together."
    },
    "Rainwater Collection": {
        "cost": {"Materials": 15, "Labor": 10},
        "produces": {"Water": 15},
        "description": "Collects and filters rainwater for community use."
    },
    "Recycling Center": {
        "cost": {"Materials": 20, "Labor": 25, "Energy": 5},
        "produces": {"Materials": 15},
        "description": "Processes recyclable materials for reuse."
    },
    "Education Center": {
        "cost": {"Materials": 30, "Labor": 20, "Energy": 5},
        "produces": {"Labor": 8},
        "description": "Educates community members and improves labor efficiency."
    },
    "Farmers Market": {
        "cost": {"Materials": 15, "Labor": 10},
        "produces": {"Food": 10, "Labor": 2},
        "description": "Allows local farmers to sell produce directly to the community."
    },
    "Water Treatment Plant": {
        "cost": {"Materials": 35, "Energy": 10, "Labor": 15},
        "produces": {"Water": 25},
        "description": "Purifies water for safe drinking and irrigation."
    }
}

# Achievements with requirements
ACHIEVEMENTS = {
    "First Building": {
        "description": "Build your first community structure",
        "requirement": {"total_buildings": 1},
        "points": 10
    },
    "Resource Diversifier": {
        "description": "Have at least one of each resource type",
        "requirement": {"all_resources": 1},
        "points": 20
    },
    "Energy Baron": {
        "description": "Produce at least 30 energy per turn",
        "requirement": {"resource_production": {"Energy": 30}},
        "points": 25
    },
    "Water Guardian": {
        "description": "Produce at least 30 water per turn",
        "requirement": {"resource_production": {"Water": 30}},
        "points": 25
    },
    "Master Builder": {
        "description": "Build 10 different structures",
        "requirement": {"total_buildings": 10},
        "points": 50
    },
    "Balanced Community": {
        "description": "Have at least 3 of each building type",
        "requirement": {"each_building": 3},
        "points": 75
    },
    "Self-Sufficient": {
        "description": "Produce at least 20 of each resource type per turn",
        "requirement": {"all_resources_min": 20},
        "points": 100
    }
}

def initialize_game_state():
    """Initialize the game state if it doesn't exist"""
    if 'game_state' not in st.session_state:
        # Check if there's saved data
        if os.path.exists(GAME_DATA_FILE):
            with open(GAME_DATA_FILE, 'r') as f:
                st.session_state.game_state = json.load(f)
        else:
            # Initialize new game state
            st.session_state.game_state = {
                "resources": {resource: 20 for resource in RESOURCE_TYPES},
                "buildings": {},
                "turn": 1,
                "achievements": [],
                "achievement_points": 0,
                "team_name": "",
                "players": []
            }
    
    if 'show_rules' not in st.session_state:
        st.session_state.show_rules = True

def save_game_state():
    """Save the current game state to file"""
    with open(GAME_DATA_FILE, 'w') as f:
        json.dump(st.session_state.game_state, f)

def add_building(building_type):
    """Add a building to the community"""
    game_state = st.session_state.game_state
    
    # Check if resources are available
    can_build = True
    for resource, amount in BUILDINGS[building_type]["cost"].items():
        if game_state["resources"].get(resource, 0) < amount:
            can_build = False
            st.error(f"Not enough {resource} to build {building_type}")
            break
    
    if can_build:
        # Deduct resources
        for resource, amount in BUILDINGS[building_type]["cost"].items():
            game_state["resources"][resource] -= amount
        
        # Add building
        if building_type not in game_state["buildings"]:
            game_state["buildings"][building_type] = 0
        game_state["buildings"][building_type] += 1
        
        st.success(f"Built 1 {building_type}")
        
        # Check achievements
        check_achievements()
        
        # Save game state
        save_game_state()

def next_turn():
    """Process the next turn"""
    game_state = st.session_state.game_state
    
    # Add resources from buildings
    for building_type, count in game_state["buildings"].items():
        for resource, amount in BUILDINGS[building_type]["produces"].items():
            game_state["resources"][resource] = game_state["resources"].get(resource, 0) + (amount * count)
    
    # Increment turn
    game_state["turn"] += 1
    
    # Check achievements
    check_achievements()
    
    # Save game state
    save_game_state()
    
    # Show success message
    st.success(f"Turn {game_state['turn']} completed!")

def check_achievements():
    """Check and award achievements"""
    game_state = st.session_state.game_state
    
    for achievement, details in ACHIEVEMENTS.items():
        # Skip if already achieved
        if achievement in game_state["achievements"]:
            continue
        
        achieved = True
        
        # Check requirements
        if "total_buildings" in details["requirement"]:
            total = sum(game_state["buildings"].values())
            if total < details["requirement"]["total_buildings"]:
                achieved = False
        
        if "all_resources" in details["requirement"] and achieved:
            min_value = details["requirement"]["all_resources"]
            for resource in RESOURCE_TYPES:
                if game_state["resources"].get(resource, 0) < min_value:
                    achieved = False
                    break
        
        if "resource_production" in details["requirement"] and achieved:
            for resource, amount in details["requirement"]["resource_production"].items():
                production = 0
                for building_type, count in game_state["buildings"].items():
                    if resource in BUILDINGS[building_type]["produces"]:
                        production += BUILDINGS[building_type]["produces"][resource] * count
                
                if production < amount:
                    achieved = False
                    break
        
        if "each_building" in details["requirement"] and achieved:
            min_count = details["requirement"]["each_building"]
            for building in BUILDINGS:
                if game_state["buildings"].get(building, 0) < min_count:
                    achieved = False
                    break
        
        if "all_resources_min" in details["requirement"] and achieved:
            min_value = details["requirement"]["all_resources_min"]
            for resource in RESOURCE_TYPES:
                production = 0
                for building_type, count in game_state["buildings"].items():
                    if resource in BUILDINGS[building_type]["produces"]:
                        production += BUILDINGS[building_type]["produces"][resource] * count
                
                if production < min_value:
                    achieved = False
                    break
        
        # Award achievement if all requirements met
        if achieved:
            game_state["achievements"].append(achievement)
            game_state["achievement_points"] += details["points"]
            st.balloons()
            st.success(f"Achievement Unlocked: {achievement} (+{details['points']} points)")

def reset_game():
    """Reset the game state"""
    if os.path.exists(GAME_DATA_FILE):
        os.remove(GAME_DATA_FILE)
    
    if 'game_state' in st.session_state:
        del st.session_state.game_state
    
    initialize_game_state()

def render_game():
    """Render the sustainability game UI"""
    initialize_game_state()
    game_state = st.session_state.game_state
    
    # Game header
    st.title("Sustainable Community Builder")
    st.subheader("Manage resources and build a sustainable community")
    
    # Setup team if not done
    if not game_state["team_name"]:
        st.header("Team Setup")
        with st.form("team_setup"):
            team_name = st.text_input("Team Name")
            players = st.text_area("Player Names (one per line)")
            
            submitted = st.form_submit_button("Start Game")
            if submitted and team_name:
                game_state["team_name"] = team_name
                game_state["players"] = [p.strip() for p in players.split("\n") if p.strip()]
                save_game_state()
                st.rerun()
        
        return
    
    # Show/hide rules
    with st.expander("Game Rules", expanded=st.session_state.show_rules):
        st.markdown("""
        ### How to Play
        1. **Manage Resources**: You start with a limited amount of resources.
        2. **Build Structures**: Use resources to build community structures.
        3. **Generate Resources**: Each turn, your structures produce resources.
        4. **Complete Achievements**: Earn points by meeting community goals.
        5. **Sustainability**: Create a balanced, self-sufficient community.
        
        ### Winning the Game
        The game is won when your team reaches 200 achievement points, 
        representing a fully sustainable community.
        """)
        if st.session_state.show_rules:
            st.session_state.show_rules = False
    
    # Game status
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"Team: {game_state['team_name']}")
    with col2:
        st.info(f"Turn: {game_state['turn']}")
    with col3:
        st.info(f"Achievement Points: {game_state['achievement_points']}")
    
    # Check win condition
    if game_state['achievement_points'] >= 200:
        st.balloons()
        st.success("🎉 CONGRATULATIONS! You've created a fully sustainable community! 🎉")
    
    # Main game area
    tab1, tab2, tab3 = st.tabs(["Resources & Building", "Achievements", "Community Status"])
    
    with tab1:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Resources")
            for resource, amount in game_state["resources"].items():
                st.metric(resource, amount)
            
            st.button("Next Turn", on_click=next_turn)
        
        with col2:
            st.subheader("Build Structures")
            
            # Building selection
            selected_building = st.selectbox("Select structure to build:", list(BUILDINGS.keys()))
            
            # Show building info
            st.write(f"**Description:** {BUILDINGS[selected_building]['description']}")
            
            # Show costs
            st.write("**Costs:**")
            for resource, amount in BUILDINGS[selected_building]["cost"].items():
                st.write(f"- {resource}: {amount}")
            
            # Show production
            st.write("**Produces per turn:**")
            for resource, amount in BUILDINGS[selected_building]["produces"].items():
                st.write(f"- {resource}: {amount}")
            
            # Build button
            st.button("Build", on_click=add_building, args=(selected_building,))
    
    with tab2:
        st.subheader("Achievements")
        
        # Show achieved
        st.write("**Completed Achievements:**")
        if game_state["achievements"]:
            for achievement in game_state["achievements"]:
                st.success(f"{achievement} (+{ACHIEVEMENTS[achievement]['points']} points): {ACHIEVEMENTS[achievement]['description']}")
        else:
            st.info("No achievements yet. Build structures and manage resources to earn achievements!")
        
        # Show available achievements
        st.write("**Available Achievements:**")
        for achievement, details in ACHIEVEMENTS.items():
            if achievement not in game_state["achievements"]:
                st.info(f"{achievement} (+{details['points']} points): {details['description']}")
    
    with tab3:
        st.subheader("Community Status")
        
        # Buildings overview
        st.write("**Buildings:**")
        if game_state["buildings"]:
            # Create a DataFrame for buildings
            building_data = []
            for building, count in game_state["buildings"].items():
                produces = ", ".join([f"{resource}: {amount * count}/turn" for resource, amount in BUILDINGS[building]["produces"].items()])
                building_data.append({
                    "Building": building,
                    "Count": count,
                    "Produces": produces
                })
            
            st.table(pd.DataFrame(building_data))
        else:
            st.info("No buildings yet. Start building to develop your community!")
        
        # Resource production
        st.write("**Resource Production per Turn:**")
        production = {resource: 0 for resource in RESOURCE_TYPES}
        
        for building, count in game_state["buildings"].items():
            for resource, amount in BUILDINGS[building]["produces"].items():
                production[resource] += amount * count
        
        # Create pie chart for resource production
        production_data = {"Resource": [], "Production": []}
        for resource, amount in production.items():
            if amount > 0:
                production_data["Resource"].append(resource)
                production_data["Production"].append(amount)
        
        if any(amount > 0 for amount in production.values()):
            chart_data = pd.DataFrame(production_data)
            st.bar_chart(chart_data.set_index("Resource"))
        else:
            st.info("No resources being produced yet. Build more structures!")
    
    # Admin controls
    with st.expander("Game Admin Controls"):
        st.warning("Warning: These actions cannot be undone!")
        if st.button("Reset Game"):
            reset_game()
            st.rerun()

def main():
    render_game()

if __name__ == "__main__":
    main()

1.	data_manager.py - JSON file-based data management (legacy)
import pandas as pd
import json
import os
import streamlit as st
from datetime import datetime

# File path constants
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "dairy_collection_data.json")

def ensure_data_dir():
    """Ensure data directory exists"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data():
    """Load data from JSON file"""
    ensure_data_dir()
    
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return []

def save_data(data):
    """Save data to JSON file"""
    ensure_data_dir()
    
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

def add_entry(entry_data):
    """Add a new entry to the data"""
    data = load_data()
    
    # Add timestamp
    entry_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data.append(entry_data)
    return save_data(data)

def delete_entry(index):
    """Delete an entry by index"""
    data = load_data()
    
    if 0 <= index < len(data):
        data.pop(index)
        return save_data(data)
    
    return False

def update_entry(index, updated_data):
    """Update an entry by index"""
    data = load_data()
    
    if 0 <= index < len(data):
        data[index] = updated_data
        return save_data(data)
    
    return False

def get_data_as_dataframe():
    """Get data as pandas DataFrame"""
    data = load_data()
    
    if data:
        return pd.DataFrame(data)
    
    return pd.DataFrame()

def export_data_as_csv():
    """Export data as CSV"""
    df = get_data_as_dataframe()
    
    if not df.empty:
        return df.to_csv(index=False).encode('utf-8')
    
    return None

def export_data_as_json():
    """Export data as JSON"""
    data = load_data()
    
    if data:
        return json.dumps(data, ensure_ascii=False, indent=4)
    
    return None
