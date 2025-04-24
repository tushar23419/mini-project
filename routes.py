from flask import Blueprint, request, jsonify
from models import db, Farmer, Dealer, Crop, Bid

main = Blueprint('main', __name__)

@main.route('/add_crop', methods=['POST'])
def add_crop():
    data = request.get_json()
    new_crop = Crop(
        name=data['name'],
        price=data['price'],
        farmer_id=data['farmer_id']
    )
    db.session.add(new_crop)
    db.session.commit()
    return jsonify({"message": "Crop added!"}), 201

@main.route('/add_bid', methods=['POST'])
def add_bid():
    data = request.get_json()
    new_bid = Bid(
        price=data['price'],
        transport_fee=data['transport_fee'],
        dealer_id=data['dealer_id'],
        crop_id=data['crop_id']
    )
    db.session.add(new_bid)
    db.session.commit()
    return jsonify({"message": "Bid placed!"}), 201

@main.route('/crop/<int:crop_id>/bids', methods=['GET'])
def get_bids(crop_id):
    bids = Bid.query.filter_by(crop_id=crop_id).all()
    bids_data = [{
        "id": bid.id,
        "price": bid.price,
        "transport_fee": bid.transport_fee,
        "dealer_name": Dealer.query.get(bid.dealer_id).name,
        "total_price": bid.price + bid.transport_fee
    } for bid in bids]
    return jsonify(bids_data), 200