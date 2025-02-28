from pydantic import BaseModel


class Vehicle(BaseModel):
    model_name: str
    driver_name: str
    plate_code: str
    brand_name: str
    year: str | None = None
    color: str

    def print_data(self):
        return f"""
            Vehicle's Model: {self.model_name}
            Driver's Name: {self.driver_name}
            Plate Code: {self.plate_code}
            Brand Name: {self.brand_name}
            Release Year: {self.year}
            Vehicle's Color: {self.color}
        """
