import math


average_car_co2_emission_in_one_year = 4600  # [kg] stala
average_oxygen_production_in_one_year = 66  # [kg] stala
oxygen_per_person_one_day = 0.28  # [kg] stala
iphone14_weight = 0.172  # [kg] stala



def mass_calculation(density, height, diameter):
    """ Calculate mass of the tree """
    radius = diameter/2
    volume = math.pi * (radius**2) * height
    mass = density * volume

    return mass


def years_of_tree_growth(diameter, growth_rate_per_year):
    """ Calculate years of tree growth """
    years = (2*math.pi*(diameter/2))/growth_rate_per_year

    return years


def dry_mass_calculation(mass):
    """ Calculate dry weight """
    dry_mass = mass/2

    return dry_mass


def current_carbon_tree_absorption(dry_mass, CO2_in_1kg_of_carbon):
    """ Calculate current CO2 tree absorption """
    current_co2_tree_absorption = dry_mass * CO2_in_1kg_of_carbon

    return round(current_co2_tree_absorption,2)


def carbon_tree_absorption_in_one_year(current_co2_tree_absorption, years_of_tree_growth):
    """ Calculate CO2 tree absorption in one year """
    co2_tree_absorption_one_year = current_co2_tree_absorption/years_of_tree_growth

    return round(co2_tree_absorption_one_year,2)


def carbon_tree_absorption_in_next_10_years(co2_tree_absorption_one_year):
    """ Calculate CO2 tree absorption in next 10 years """
    co2_tree_absorption_next_ten_years = co2_tree_absorption_one_year * 10

    return round(co2_tree_absorption_next_ten_years)


def current_oxygen_tree_production(years):
    """ Calculate oxygen tree prodution in one year """
    current_oxygen_tree_production = years * average_oxygen_production_in_one_year

    return round(current_oxygen_tree_production,2)


def oxygen_tree_production_in_next_10_years():
    """ Calculate oxygen tree production in the next 10 years """
    oxygen_tree_production_in_next_ten_years = average_oxygen_production_in_one_year * 10

    return round(oxygen_tree_production_in_next_ten_years,2)


def oxygen_days_for_one_person(current_oxygen_tree_production):
    """ Calculate how many days for one person produce the tree """
    oxygen_days_one_person = current_oxygen_tree_production/oxygen_per_person_one_day

    return round(oxygen_days_one_person,2)


def years_car_emission(current_co2_tree_absorption):
    """ Calculate how many years for car emission absorbe the tree """
    years_car_emission = current_co2_tree_absorption / \
        average_car_co2_emission_in_one_year

    return round(years_car_emission,2)


def how_many_smartphones(current_co2_tree_absorption):
  """ Calculate how many years for car emission absorbe the tree """
  smartphone_number = round(current_co2_tree_absorption/iphone14_weight, 2)

  return round(smartphone_number,2)


def carbon_tree_absorption_in_next_10_years(co2_tree_absorption_one_year):
  """ Calculate CO2 tree absorption in next 10 years """
  co2_tree_absorption_next_ten_years = co2_tree_absorption_one_year * 10

  return round(co2_tree_absorption_next_ten_years,2)


def oxygen_years_for_one_person(current_oxygen_tree_production):
  """ Calculate how many days for one person produce the tree """
  oxygen_years_one_person = round(
      current_oxygen_tree_production/oxygen_per_person_one_day/365, 2)

  return oxygen_years_one_person
