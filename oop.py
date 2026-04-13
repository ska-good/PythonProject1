# Задача 6

from enum import Enum
from typing import List, Iterator


class RoomType(Enum):
    ECONOMY = "одноместный"
    COMFORT = "двухместный"
    COMFORT_PLUS = "трехместный"
    LUXURY = "люкс"


class Room:
    def __init__(self, room_number: int, room_type: RoomType, price: int, is_booked: bool):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self._is_booked = is_booked

    @property
    def is_booked(self):
        return self._is_booked

    def book(self) -> None:
        """Бронирует комнату, если она свободна"""
        if not self._is_booked:
            self._is_booked = True
            print(f"✅ Комната {self.room_number} успешно забронирована")
        else:
            print(f"❌ Комната {self.room_number} уже забронирована")

    def cancel_booking(self) -> None:
        """Отменяет бронирование комнаты"""
        if self._is_booked:
            self._is_booked = False
            print(f"✅ Бронирование комнаты {self.room_number} отменено")
        else:
            print(f"❌ Комната {self.room_number} не была забронирована")

    def is_available(self) -> bool:
        """Возвращает True, если комната свободна, False - если забронирована"""
        return not self._is_booked

    # НОВЫЙ МЕТОД: __eq__ для сравнения комнат
    def __eq__(self, other) -> bool:
        """
        Сравнивает две комнаты.
        Комнаты считаются одинаковыми, если у них совпадает номер.
        """
        if not isinstance(other, Room):
            return NotImplemented
        return self.room_number == other.room_number

    def __str__(self):
        status = "🔴 Забронирована" if self._is_booked else "🟢 Свободна"
        return f"Комната {self.room_number} ({self.room_type.value}) - {self.price}₽/сутки - {status}"

    # НОВЫЙ МЕТОД: __repr__ для технического представления
    def __repr__(self):
        """Техническое представление комнаты для разработчиков"""
        return f"Room(room_number={self.room_number}, room_type={self.room_type.name}, price={self.price}, is_booked={self._is_booked})"


class LuxuryRoom(Room):
    def __init__(self, room_number: int, room_type: RoomType, price: int, is_booked: bool, jacuzzi_size: str):
        if room_type != RoomType.LUXURY:
            print(f"⚠️ Предупреждение: комната {room_number} создана как LuxuryRoom, но тип {room_type.value}")

        super().__init__(room_number, room_type, price, is_booked)
        self.jacuzzi_size = jacuzzi_size

    def __str__(self):
        jacuzzi_icon = {"S": "🛁", "M": "🛁🛁", "L": "🛁🛁🛁"}
        icon = jacuzzi_icon.get(self.jacuzzi_size, "🛁")
        return super().__str__() + f" - Джакузи {icon} ({self.jacuzzi_size})"

    def __repr__(self):
        """Техническое представление люксовой комнаты для разработчиков"""
        return f"LuxuryRoom(room_number={self.room_number}, room_type={self.room_type.name}, price={self.price}, is_booked={self._is_booked}, jacuzzi_size='{self.jacuzzi_size}')"


class Hotel:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.rooms: List[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)
        print(f"Комната {room.room_number} добавлена в отель '{self.name}'")

    def add_rooms(self, *rooms: Room) -> None:
        for room in rooms:
            self.add_room(room)

    def get_available_rooms(self) -> List[Room]:
        return [room for room in self.rooms if room.is_available()]

    def show_available_rooms(self) -> None:
        available = self.get_available_rooms()

        print("\n" + "=" * 60)
        print(f"🏨 {self.name} ({self.location})")
        print("=" * 60)

        if not available:
            print("❌ К сожалению, нет доступных номеров.")
        else:
            print(f"✅ Доступные номера ({len(available)} шт.):")
            print("-" * 60)
            for room in available:
                print(f"  • {room}")
        print("=" * 60 + "\n")

    def calculate_total_price_per_day(self) -> int:
        available_rooms = self.get_available_rooms()
        total_price = sum(room.price for room in available_rooms)

        print(f"💰 Общая стоимость всех доступных номеров за 1 день: {total_price}₽")
        print(f"   (Всего свободно {len(available_rooms)} номеров)")

        return total_price

    # НОВЫЙ МЕТОД: __len__ для получения количества номеров
    def __len__(self) -> int:
        """
        Возвращает общее количество номеров в отеле.
        Позволяет использовать функцию len(hotel).
        """
        return len(self.rooms)

    # НОВЫЙ МЕТОД: __iter__ для итерации по номерам
    def __iter__(self) -> Iterator[Room]:
        """
        Возвращает итератор по номерам отеля.
        Позволяет использовать for room in hotel.
        """
        return iter(self.rooms)

    # НОВЫЙ МЕТОД: __contains__ для проверки наличия комнаты
    def __contains__(self, room: Room) -> bool:
        """
        Проверяет, есть ли переданная комната в отеле.
        Позволяет использовать оператор 'in'.
        """
        return room in self.rooms

    # НОВЫЙ МЕТОД: __str__ для красивого представления отеля
    def __str__(self) -> str:
        """
        Пользовательское представление отеля.
        Вызывается при print(hotel) или str(hotel).
        """
        available_count = len(self.get_available_rooms())
        return f"Отель '{self.name}' в {self.location}: {len(self.rooms)} номеров, {available_count} свободно"

    # НОВЫЙ МЕТОД: __repr__ для технического представления отеля
    def __repr__(self) -> str:
        """
        Техническое представление отеля для разработчиков.
        Вызывается при repr(hotel) или в интерактивной консоли.
        """
        return f"Hotel(name='{self.name}', location='{self.location}', rooms={repr(self.rooms)})"


# ========== ДЕМОНСТРАЦИЯ РАБОТЫ ==========

if __name__ == "__main__":
    print("=" * 70)
    print("🏨 ДЕМОНСТРАЦИЯ НОВЫХ МЕТОДОВ")
    print("=" * 70)

    # Создаём отель
    hotel = Hotel("Grand Plaza", "Москва, ул. Тверская, 10")

    # Создаём комнаты
    room1 = Room(101, RoomType.ECONOMY, 5000, False)
    room2 = Room(102, RoomType.COMFORT, 8000, True)
    room3 = Room(103, RoomType.COMFORT_PLUS, 10000, False)
    luxury1 = LuxuryRoom(201, RoomType.LUXURY, 20000, False, "S")
    luxury2 = LuxuryRoom(202, RoomType.LUXURY, 25000, True, "M")

    # Добавляем комнаты
    hotel.add_rooms(room1, room2, room3, luxury1, luxury2)

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ __str__ И __repr__")
    print("=" * 70)

    # Демонстрация __str__ (для пользователей)
    print("\n1. __str__ для отеля (print(hotel)):")
    print(hotel)

    print("\n2. __str__ для комнаты (print(room1)):")
    print(room1)
    print(room2)
    print(luxury1)

    # Демонстрация __repr__ (для разработчиков)
    print("\n3. __repr__ для отеля (repr(hotel)):")
    print(repr(hotel))

    print("\n4. __repr__ для комнаты (repr(room1)):")
    print(repr(room1))
    print(repr(luxury1))

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ __len__")
    print("=" * 70)
    print(f"Всего номеров в отеле: {len(hotel)}")

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ __iter__")
    print("=" * 70)
    print("Перебираем все номера отеля (for room in hotel):")
    for i, room in enumerate(hotel, 1):
        print(f"  {i}. {room}")

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ __contains__")
    print("=" * 70)

    # Проверяем наличие комнат
    print(f"Комната 101 в отеле? {room1 in hotel}")  # Должно быть True
    print(f"Комната 102 в отеле? {room2 in hotel}")  # Должно быть True
    print(f"Комната 999 в отеле? {Room(999, RoomType.ECONOMY, 1000, False) in hotel}")  # Должно быть False

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ __eq__")
    print("=" * 70)

    # Создаём комнату с таким же номером
    room1_copy = Room(101, RoomType.ECONOMY, 5500, True)  # Другой объект, но номер 101
    room_different = Room(999, RoomType.ECONOMY, 1000, False)

    print(f"room1 и room1_copy (один номер 101) равны? {room1 == room1_copy}")
    print(f"room1 и room_different (разные номера) равны? {room1 == room_different}")
    print(f"room1 и None равны? {room1 == None}")

    print("\n" + "=" * 70)
    print("📋 ДЕМОНСТРАЦИЯ ВСЕХ МЕТОДОВ ВМЕСТЕ")
    print("=" * 70)

    # Комбинируем все возможности
    print(f"Отель: {hotel}")
    print(f"Всего номеров: {len(hotel)}")
    print(f"Свободных номеров: {len(hotel.get_available_rooms())}")
    print(f"Есть ли комната 101? {'Да' if room1 in hotel else 'Нет'}")

    print("\nСписок всех номеров:")
    for room in hotel:
        print(f"  • {room}")

