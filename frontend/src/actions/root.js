export const screens = {
	DASH: 'DASH',
	STUDENT: 'STUDENT',
	COUNTRY: 'COUNTRY',
	STATE: 'STATE',
	SCHOOL: 'SCHOOL',
	DISTRICT: 'DISTRICT',
}

export const CHANGE_SCREEN = 'CHANGE_SCREEN'

export const changeScreen = screen => ({
	type: CHANGE_SCREEN,
	screen: screen, 
})