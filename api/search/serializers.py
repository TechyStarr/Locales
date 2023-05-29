from ..models.data import State, Region

def serialized_state(state):
    return {
        'id': state.id,
        'name': state.name,
        'region_id': state.region_id,
        'capital': state.capital,
        'population': state.population,
        'area': state.area,
        'postal_code': state.postal_code,
        'No_of_LGAs': state.No_of_LGAs,
        'local_government_areas': state.local_government_areas
    }
