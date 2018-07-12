// Сделал на чистом js, кроме запросов, поскольку в задании не было требований к фреймворкам
// Да и просто было интересно попробовать
// Если нужно, могу переделать с применением Angular или Backbone

class Symbol {
	constructor(name, price, precent, change, offset, witdh) {
		this.name = name;
		this.price = price;
		this.precent = precent;
		this.change = change;
		this._width = witdh; // Ширина блока
		this._offset = offset; // Отступ блока
		this._up = change > 0 ? true : false // Растет ли курс
		this.makeDiv(); // Создание блока
		this.makeStats(); // Создание значений внутри блока
		this.insertInLine(); // Добавление блока в бегущую строку
	}

	makeDiv() {
		let symbol_box = document.createElement('div');
		symbol_box.className = 'symbol';
		this._box = symbol_box;
	}

	makeStats() {
		//Без шаблонизаторов получается страшно :(
		let priceSpan = document.createElement('span');
		priceSpan.className = 'price';
		priceSpan.textContent = this.price;
		let changeSpan = document.createElement('span');
		changeSpan.className = 'change';
		changeSpan.textContent = this.change;
		let precentSpan = document.createElement('span');
		precentSpan.className = 'precent';
		precentSpan.textContent = this.precent;
		let nameSpan = document.createElement('span');
		nameSpan.className = 'name';
		nameSpan.textContent = this.name;
		this._box.appendChild(priceSpan);
		this._box.appendChild(precentSpan);
		this._box.appendChild(nameSpan);
		this._box.appendChild(changeSpan);
		this.setColors(changeSpan, precentSpan)
	}

	insertInLine() {
		this._box.style.cssText = 'width: ' + this._width + 'px;' +
								  'left: ' +  this._offset + 'px;'
		symbol_boxes.push(this._box);
		symbols.push(this);
		running_string.appendChild(this._box);
	}

	setColors(change, precent) {
		if (this._up) {
			change.classList.add('up');
			precent.classList.add('up');
			precent.classList.add('arrow_up');
		} else {
			change.classList.add('down');
			precent.classList.add('down');
			precent.classList.add('arrow_down');
		}
	}

	setDefaultPosition() {
		// При изменении размера окна ставит блок на начальную позицию
		this._box.style.left = this._offset + 'px';
	}
}

let meter = new FPSMeter();

let running_string = document.getElementById('running');
const symbol_boxes = [];
const symbols = [];
let witdh = 250; // Ширина блоков
let speed = 1; // Скорость блоков

function getData() {
	$.ajax({
		method: 'GET',
		url: window.location.href + 'api/v1/symbols/list',
		datatype: 'json',
		success: function(data) {
			for (var i = 0; i <= data.length - 1; i++) {
				let s = new Symbol(data[i].name, data[i].price, data[i].precent, data[i].delta, witdh * i, witdh)
			}
		},
		error: function(e) {
			console.log(e);
		}
	})
}

function animation() {
	let timerId = setInterval(function() {
		symbol_boxes.map(function(item, index) {
			let bounds = item.getBoundingClientRect()
			item.style.left = bounds.left - speed + 'px';
			if (bounds.left < -witdh && document.documentElement.clientWidth > (symbol_boxes.length - 1)  * witdh) {
				if (index === 0) {
					item.style.cssText += "border-left: 1px solid #57e5e0;";
				}
				item.style.left = document.documentElement.clientWidth + 'px';
			} else if ( bounds.left < -witdh && document.documentElement.clientWidth < (symbol_boxes.length - 1) * witdh) {
				item.style.left = (symbol_boxes.length - 1) * witdh - speed * 2 + 'px';
				if (index === 0) {
					item.style.borderLeft = "";
				}
			} 
		})
		meter.tick();
	}, 16)

	return timerId
}


window.onload = function() {
	getData(); // Получение данных
	let timerId = animation(); // Начало анимации и возврат timerID для остановки интервала

	window.onresize = function() {
		clearTimeout(timerId); // Остановка анимации
		symbols.map(function(item, index) {
			item.setDefaultPosition(); // Расстановка на начальные позиции
		});
		timerId = animation();  // Запуск анимации
	}
}

