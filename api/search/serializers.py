from ..models.data import State, Region, Lga

def serialized_region(region):
    return {
        'id': region.id,
        'name': region.name,
    }



def serialized_state(state):
    return {
        'id': state.id,
        'name': state.name,
        'region_id': state.region_id,
        'capital': state.capital,
        'population': state.population,
        'area': state.area,
        'postal_code': state.postal_code,
        # 'No_of_LGAs': state.No_of_LGAs,
        'lgas': state.lgas
    }


def serialized_lga(lga):
    return {
        'id': lga.id,
        'name': lga.name,
        'state_id': lga.state_id,
        'state': lga.state,
        'senatorial_district': lga.senatorial_district,
        'area': lga.area,
        'population': lga.population,
        'headquarters': lga.headquarters
    }

